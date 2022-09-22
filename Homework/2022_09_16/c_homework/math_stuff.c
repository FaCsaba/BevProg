#include <math.h>
#include <stdio.h>
#include <stdint.h>

typedef struct Vec2 {
    double x;
    double y;
} Vec2;

struct Vec2 quadratic_equation(double a, double b, double c) {
    double discriminator = sqrt(b * b - 4 * a * c);
    Vec2 ret = {
        .x = (-b + discriminator) / (a * 2),
        .y = (-b - discriminator) / (a * 2)
    };
    return ret;
}

typedef struct WV {
    uint64_t weight;
    uint64_t value;
} WV;

double weighted_average(struct WV* wv, int arr_length ) {
    uint64_t weighted_value = 0;
    for (int i=0; i < arr_length; i++) {
        weighted_value += wv[i].weight * wv[i].value;
    }

    uint64_t sum_of_weight = 0;
    for (int i=0; i < arr_length; i++) {
        sum_of_weight += wv[i].weight;
    }

    return (double)weighted_value / (double)sum_of_weight;
}

double standard_deviation(int l[], int length) {
    int sum = 0;
    for(int i = 0; i < length; i++) {
        sum += l[i];
    }
    double average = (double)sum / (double)length;
    double s = 0;
    for(int i = 0; i < length; i++) {
        s += pow(fabs(l[i] - average), 2.0);
    }
    return sqrt(s / length);
}

int main() {
    Vec2 t = quadratic_equation(2, -5, -6);
    printf("%.5f, %.5f\n", t.x, t.y);
    WV wv_array[2] = {{.weight = 25, .value = 75}, {.weight = 30, .value = 60}};
    double a = weighted_average(wv_array, 2);
    printf("%f\n", a);
    int sda[20] = {9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4};
    double sd = standard_deviation(sda, 20);
    printf("%f\n", sd);
    return 0;
}