int strStr(char* haystack, char* needle) {
    int h = strlen(haystack);
    int n = strlen(needle);
    if (n > h) {
        return -1;
    }
    int i = 0, j = 0, index = 0;
    while (i < h && j < n) {
        if (haystack[i] == needle[j]) {
            if (j == n - 1) {
                return index;
            }
            i++;
            j++;
        } else {
            i = index + 1;
            j = 0;
            index = i;
        }
    }
    return -1;
}
