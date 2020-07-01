/* TDS Util ISF file to CSV file converter
   revision 0.001
   Copyright (c) 1992 Tektronix Inc.
   All rights reserved.

   Compiled with Microsoft 'C' version 7.0
*/
#include <stdio.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

//#define DEBUG

int bUOption = 0 ;         /* True if unscaled data is required */

/* This variables are used to contain information about the waveform. They
   are used by several of the functions that follow.
*/
int bEnvelop = 0 ;         /* True if this is an envelop */
long   lNumPoints ;             /* The number of points in the array   */
double dXIncr   ;               /* Delta X between points */
double dYMult   ;
double dYOff    ;
double dPtoff   ;
double dYZero   ;


int FindAndGetFloat(char *szBuffer, char *szId, double *dValue)
    {
    /* Search the buffer 'szBuffer' for the string 'szId', extract the
       number immediately after it and convert it to a double pointed to
       by 'dValue'.

       szBuffer - pointer to NUL terminated string containing the waveform
                    preable.

       szId - pointer NUL terminated string containing the string to search
                    for.

        dValue - a pointer to the double that will contain the result of the
                    function.
                    
       result - 1 if the string pointed at by 'szId' is found, else 0.
    */
    char *pszFound ;

    pszFound = strstr(szBuffer, szId) ;
    if ( pszFound == NULL )
        {
        printf("*** Error - this is not a TDS Utility ISF file!\n") ;
        return 0 ;
        }

    pszFound += strlen(szId) ;
    *dValue = atof(pszFound) ;
    return 1 ;
    }
    
int ExtractHeaderInfo(int iHandle)
    {
    /* We will read in the first 511 bytes, its always at least 511 bytes long,
       then extract the header information and reposition the file at the
       first data byte.

       iHandle is the handle of the input file.

       result - 1 if no errors found, else 0.
    */
    #define WAIT_WARN_POINT     1500
    char *pszBuffer ;
    int   iStat ;
    char *pszFound  ;
    double dTemp    ;
    
    pszBuffer = malloc(512) ;
    if ( pszBuffer == NULL )
        {
        printf("*** Error - unable to allocate memory?\n") ;
        return 0 ;
        }
    iStat = read(iHandle, pszBuffer, 512) ;
    if ( iStat != 512 )
        {
        printf("*** Error - Unable to read header from input file.\n") ;
        return 0 ;
        }
    pszBuffer[511] = '\0' ;

    /* Now find the information we need */
    pszFound = strstr(pszBuffer, "Envelope") ;
    if ( pszFound != NULL )
        bEnvelop = 1 ;

    if ( !FindAndGetFloat(pszBuffer, "XINCR", &dXIncr) )
        return 0 ;

    if ( !FindAndGetFloat(pszBuffer, "PT_OFF", &dPtoff) )
        return 0 ;
        
    if ( !FindAndGetFloat(pszBuffer, "YMULT", &dYMult) )
        return 0 ;
        
    if ( !FindAndGetFloat(pszBuffer, "YOFF", &dYOff) )
        return 0 ;

    if ( !FindAndGetFloat(pszBuffer, "YZERO", &dYZero) )
        return 0 ;

    if ( !FindAndGetFloat(pszBuffer, "NR_PT", &dTemp) )
        return 0 ;
    lNumPoints = (long)dTemp ;

    if ( lNumPoints > WAIT_WARN_POINT )
//        printf("\n--- This will take a little while.---\n") ;

    /* Reposition the file */
    lseek(iHandle, 0L, SEEK_SET) ;
    return 1 ;
    }

int AdvanceToData(int iHandle)
    {
    /* Move the file position to just before the first data point.

        iHandle - Handle to the input file.

        result - 0 if an error was encountered, else 1.
    */
    char c ;
    int  iStat ;
    int  iNumDigits ;

    /* Find the '#' the marks the binary field */
    c = ' ' ;
    while ( c != '#' )
        {
        iStat = read(iHandle, &c, 1) ;
        if ( iStat != 1 )
            {
            printf("*** Error - reading the input file.\n") ;
            return 0 ;
            }
        }

    /* The value in variable 'c' is the ASCII for the number of digits
       to skip over.
    */
    iStat = read(iHandle, &c, 1) ;
    if ( iStat != 1 )
        {
        printf("*** Error - reading the input file.\n") ;
        return 0 ;
        }
    iNumDigits = (int)(c - '0') ;
    while (iNumDigits > 0 )
        {
        iStat = read(iHandle, &c, 1) ;
        if ( iStat != 1 )
            {
            printf("*** Error - reading the input file.\n") ;
            return 0 ;
            }
        --iNumDigits ;
        }
    return 1 ;
    }    

int UnscaledSimple(int iInFileHandle, FILE *fOutFile) 
    {
    /* 'iInFileHandle' is the handle to a file position at the data.
        fOutFile is a file point to the output file.

        The data will be written as:
        xxx,yyy
        where 'xxx' is the number of the point and 'yyy' is the digitizer level
            from the scope.  Scale, offset and YZero are not applied.   The
            values are integers.

        iInFileHandle - the handle of the input file.

        fOutFile - file pointer for the output file.

        result - 1 if no errors were encountered, else 0.
    */
    long lLcvPoint ;        /* Used to step through the points */
    char c ;                /* Buffer to read the point        */
    int  iPoint ;           /* Point value for printing        */
    int  iStat  ;
    
    for ( lLcvPoint=0; lLcvPoint<lNumPoints; lLcvPoint++)
        {
        if ( read(iInFileHandle, &c, 1) != 1 )
            { printf("*** Error - read data points.\n") ;
              return 0 ; }
        iPoint = (int)(c << 8);
        if ( read(iInFileHandle, &c, 1) != 1 )
            { printf("*** Error - read data points.\n") ;
              return 0 ; }
        iPoint = iPoint + (0xff & (int)c);

        iStat = fprintf(fOutFile, "%ld,%d\n", lLcvPoint, iPoint) ;
        if ( iStat < 0 )
            {
            printf("*** Error - writing output file.\n") ;
            return 0 ;
            }
        }
    return 1 ;
    }


int UnscaledEnvelop(int iInFileHandle, FILE *fOutFile) 
    {
    /* 'iInFileHandle' is the handle to a file position at the data.
        fOutFile is a file point to the output file.

        The data will be written as:
        xxx,yyy,zzzz
        where 'xxx' is the number of the point and 'yyy' is the digitizer level
            from the scope for the max and 'zzz' for the min.
            Scale, offset and YZero are not applied. The values are integers.

        iInFileHandle - the handle of the input file.

        fOutFile - file pointer for the output file.

        result - 1 if no errors were encountered, else 0.
    */
    long lLcvPoint ;  /* Used to step through the points */
    char c         ;  /* Buffer to read the point        */
    int  iPointMax ;  /* Point value for printing     */
    int  iPointMin ;  /* Point value for min          */
    int  iStat     ;
    
    for ( lLcvPoint=0; lLcvPoint<lNumPoints; )
        {
        /* Read max */
        if ( read(iInFileHandle, &c, 1) != 1 )
            { printf("*** Error - read data points.\n") ;
              return 0 ; }
        iPointMax = (int)(c << 8);
        if ( read(iInFileHandle, &c, 1) != 1 )
            { printf("*** Error - read data points.\n") ;
              return 0 ; }
        iPointMax = iPointMax + (0xff & (int)c) ;
        
        /* Read min */
        if ( read(iInFileHandle, &c, 1) != 1 )
            { printf("*** Error - read data points.\n") ;
              return 0 ; }
        iPointMin = (int)(c << 8);
        if ( read(iInFileHandle, &c, 1) != 1 )
            { printf("*** Error - read data points.\n") ;
              return 0 ; }
        iPointMin = iPointMin + (0xff & (int)c) ;

        iStat = fprintf(fOutFile, "%ld,%d,%d\n", lLcvPoint, iPointMax, iPointMin) ;
        if ( iStat < 0 )
            {
            printf("*** Error - writing output file.\n") ;
            return 0 ;
            }

        lLcvPoint += 2 ;
        }
    return 1 ;
    }


int ScaledSimple(int iInFileHandle, FILE *fOutFile) 
    {
    /* 'iInFileHandle' is the handle to a file position at the data.
        fOutFile is a file point to the output file.

        The data will be written as:
        xxx,yyy
        where 'xxx' is the time and 'yyy' is the voltage
            from the scope.  

        iInFileHandle - the handle of the input file.

        fOutFile - file pointer for the output file.

        result - 1 if no errors were encountered, else 0.
    */
    long   lLcvPoint ;      /* Used to step through the points */
    char   c         ;      /* Buffer to read the point        */
    double dPoint    ;
    double dTime     ;
    int    iStat     ;
    int    data      ;

    for ( lLcvPoint=0; lLcvPoint<lNumPoints; lLcvPoint++)
        {
        if ( read(iInFileHandle, &c, 1) != 1 )
            { printf("*** Error - read data points.\n") ;
              return 0 ; }
        data = (int)(c << 8);
        if ( read(iInFileHandle, &c, 1) != 1 )
            { printf("*** Error - read data points.\n") ;
              return 0 ; }
        data = data + (0xff & (int)c);

        dPoint = dYZero + dYMult * ((double)data - dYOff) ;
        dTime  = dXIncr*((double)lLcvPoint - dPtoff) ;
//      iStat = fprintf(fOutFile, "%lg,%g\n", dTime, dPoint) ;
		iStat = fprintf(fOutFile, "%lg\t%g\n", dTime, dPoint) ;
        if ( iStat < 0 )
            {
            printf("*** Error - writing output file.\n") ;
            return 0 ;
            }
        }
    return 1 ;
    }


int ScaledEnvelop(int iInFileHandle, FILE *fOutFile) 
    {
    /* 'iInFileHandle' is the handle to a file position at the data.
        fOutFile is a file point to the output file.

        The data will be written as:
        xxx,yyy,zzzz
        where 'xxx' is the time of the point and 'yyy' is the voltage.
            from the scope for the max and 'zzz' for the min.

        iInFileHandle - the handle of the input file.

        fOutFile - file pointer for the output file.

        result - 1 if no errors were encountered, else 0.
    */
    long   lLcvPoint ;      /* Used to step through the points */
    char   c         ;      /* Buffer to read the point        */
    double dPointMax ;
    double dPointMin ;
    double dTime     ;
    int    iStat     ;
    int    data      ;
    
    for ( lLcvPoint=0; lLcvPoint<lNumPoints; )
        {
        dTime  = dXIncr*((double)lLcvPoint - dPtoff) ;

        /* Read max */
        if ( read(iInFileHandle, &c, 1) != 1 )
            { printf("*** Error - read data points.\n") ;
              return 0 ; }
        data = (int)(c << 8);
        if ( read(iInFileHandle, &c, 1) != 1 )
            { printf("*** Error - read data points.\n") ;
              return 0 ; }
        data = data + (0xff & (int)c);
        dPointMax = dYZero + dYMult * ((double)data - dYOff) ;

        
        /* Read min */
        if ( read(iInFileHandle, &c, 1) != 1 )
            { printf("*** Error - read data points.\n") ;
              return 0 ; }
        data = (int)(c << 8);
        if ( read(iInFileHandle, &c, 1) != 1 )
            { printf("*** Error - read data points.\n") ;
              return 0 ; }
        data = data + (0xff & (int)c);
        dPointMin = dYZero + dYMult * ((double)data - dYOff) ;

        iStat = fprintf(fOutFile, "%lg,%lg,%lg\n", dTime, dPointMax, dPointMin) ;
        if ( iStat < 0 )
            {
            printf("*** Error - writing output file.\n") ;
            return 0 ;
            }

        lLcvPoint += 2 ;
        }
    return 1 ;
    }
    
int main(int argc, char *argv[])
    {
    int  iIndex ;            /* Used to scan through the command line arguments */
    int  iInFileHandle ;
    FILE *fOutFile ;

#ifdef DEBUG
    /* Print herald line */
    printf("\ntdtocsv - TDS Util ISF file to CSV file converter. Rev 0.001\n") ;
    printf("Copyright (c) 1992, Tektronix Inc.\n\n") ;
#endif
    
    /* Check the arguments on the command line */
    if ( argc < 3 )
        {
        printf("*** Error - invalid argument list:\n") ;
        printf("   td2csv [-u] infile outfile\n") ;
        return 0 ;
        }
    iIndex = 1 ;
    if ( strcmp(argv[1], "-u") == 0 ) 
        {
        bUOption = 1 ;
        ++iIndex ;
        }

        
    /* Open the input and output files */
/*    iInFileHandle = open(argv[iIndex], O_BINARY | O_RDONLY) ; */
    iInFileHandle = open(argv[iIndex], O_RDONLY) ;
    if ( iInFileHandle == -1 )
        {
        printf("*** Error - Unable to open file for input. file: \"%s\".\n", argv[iIndex]) ;
        return 0 ;
        }
    ++iIndex ;

    fOutFile = fopen(argv[iIndex], "w") ;
    if ( fOutFile == NULL )
        {
        printf("*** Error - Invalid file name for output file \"%s\".\n", argv[iIndex]) ;
        return 0 ;
        }

    if ( !ExtractHeaderInfo(iInFileHandle) )
        return 0 ;
#ifdef DEBUG
    if ( bUOption )
        {
        /* Print the header info */

			if ( bEnvelop )

            printf("Envelop\n") ;
        else
            printf("Not Envelop\n") ;
        printf("XIncr:%lg\n", dXIncr) ;
        printf("YMult:%lg\n", dYMult) ;
        printf("Ptoff:%lg\n", dPtoff) ;
        printf("YZero:%lg\n", dYZero) ;
        printf("YOff :%lg\n", dYOff)  ;
        printf("Number of samples:%ld\n", lNumPoints) ;
        printf("\nTo convert Y values to volts use the following formula:\n") ;
        printf("voltage = YZero + YMult * ( point - YOff )\n") ;
        printf("            The point should be treated as a signed integer.\n") ;
        }
#endif
    /* Advance to first data point */
    if ( !AdvanceToData(iInFileHandle) )
        return 0 ;
        
    /* Read and convert the data, line at a time */
    if ( bUOption )
        {
        /* Data to be left unscaled */
        if ( bEnvelop )
            {
            UnscaledEnvelop(iInFileHandle, fOutFile) ;
            }
        else
            {
            UnscaledSimple(iInFileHandle, fOutFile) ;
            }            
        }
    else
        {
        /* Scale the data */
        if ( bEnvelop )
            {
            ScaledEnvelop(iInFileHandle, fOutFile) ;
            }
        else
            {
            ScaledSimple(iInFileHandle, fOutFile) ;
            }            
        }

    close (iInFileHandle) ;
    fclose(fOutFile) ;
    return 1 ;
    }

    
