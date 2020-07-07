#include <dirent.h>
#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
int main(){
  DIR *dir;
  struct dirent *file;
  char fileName[255];
  char newfilename[255];
  dir = opendir(".");
    while ((file = readdir(dir)) != NULL)
    {
        //printf("  %s\n", file->d_name);
        strncpy(fileName, file->d_name, 254);
        fileName[12] = '\0';
       
         printf("%s\n", fileName);
    }
    closedir(dir);
return 0;
}