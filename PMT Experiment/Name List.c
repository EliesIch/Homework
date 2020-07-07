int main()
{
    DIR *dir;
    struct dirent *file;
    char fileName[255];
    dir = opendir(".");
    while ((file = readdir(dir)) != NULL)
    {
        printf("  %s\n", file->d_name);
        strncpy(fileName, file->d_name, 254);
        fileName[254] = '\0';
        printf("%s\n", fileName);
    }
    closedir(dir);
    return 0;
}