#include <stdio.h>

int get_na_amount() {
    int na;
    printf("How many Na-s do you have? ");
    while(!scanf("%d", &na)) {
        fseek(stdin,0,SEEK_END);
        printf("Not a number\n");

        printf("How many Na-s do you have? ");
    }
    return na;
}

int get_cl2_amount() {
    int cl2;
    printf("How many Cl\u2082-s do you have? ");
    while(!scanf("%d", &cl2)) {
        fseek(stdin,0,SEEK_END);
        printf("Not a number\n");

        printf("How many Cl\u2082-s do you have? ");
    }
    return cl2;
}

int main() {
    int na = get_na_amount();
    int cl2 = get_cl2_amount();

    int nacl = 0, excess_na = 0, excess_cl = 0;

    if (na == cl2*2) {
        nacl = na;
    }
    if (na > cl2*2) {
        nacl = cl2*2;
        excess_na = na - cl2*2;
    }
    if (cl2*2 > na) {
        nacl = na;
        excess_cl = cl2*2 - na;
    }
    printf("You can make %d NaCl, isn't that exciting?", nacl);
    if (excess_na > 0) {
        printf("But you have an excess of %d Na", excess_na);
    }
    if (excess_cl > 0) {
        printf("But you have an excess of %d Cl", excess_cl);
    }

    return 0;
}