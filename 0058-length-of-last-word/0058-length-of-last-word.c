int lengthOfLastWord(char* s) {
    char* token;
    char* last_item;
    int n;

    token = strtok(s, " ");
    while (token){
        last_item = token;
        token = strtok(NULL, " ");
    }
    n = strlen(last_item);
    return n;
}