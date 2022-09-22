#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>

const uint8_t DRINK_IN_AMERICA = 21;
const uint8_t TOBACCO_IN_HUNGARY = 18;
const uint8_t DRIVERS_LICENSE_IN_HUNGARY = 17;
const uint8_t WATCH_SHREK_2 = 12;

int main() {
    uint8_t age;
    printf("What is your age? ");
    while(!scanf("%" SCNu8, &age)) {
        fseek(stdin,0,SEEK_END);
        printf("Not a number\n");
        
        printf("What is your age? ");
    }
    if (age >= DRINK_IN_AMERICA) {
        printf("You can legally drink alcohol in America\n");
    }
    if (age >= TOBACCO_IN_HUNGARY) {
        printf("You can legally consume tobacco products in Hungary\n");
    }
    if (age >= DRIVERS_LICENSE_IN_HUNGARY) {
        printf("You can legally get a drivers license in Hungary\n");
    }
    if (age >= WATCH_SHREK_2) {
        printf("You can legally watch Shrek 2\n");
    }
}