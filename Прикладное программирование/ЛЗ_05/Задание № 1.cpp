


unsigned strlen(const char *str)
{
    if (str == 0) return 0; 
    unsigned len = 0;
    while (*str != '\0')
    {
        len++;
        str++;
    }
    return len;
}
