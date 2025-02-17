#include <stdio.h>
#include <string.h>

void backtrack(int *count, int *res) {
    for (int i = 0; i < 26; i++) {
        if (count[i] > 0) {
            (*res)++;
            count[i]--;
            backtrack(count, res);
            count[i]++;
        }
    }
}

int numTilePossibilities(char* tiles) {
    int count[26] = {0}, res = 0;
    
    // Count frequency of each character
    for (int i = 0; tiles[i] != '\0'; i++) {
        count[tiles[i] - 'A']++;
    }
    
    // Perform backtracking
    backtrack(count, &res);
    
    return res;
}
