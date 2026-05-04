#ifndef GRAPHICS_H
#define GRAPHICS_H

#include <iostream>
#include <windows.h>
#include <cmath>

using namespace std;

const int BLUE = 1;
const int WHITE = 15;
const int RED = 4;
const int GREEN = 2;
const int BLACK = 0;
const int DETECT = 0;

HWND hwnd = NULL;
HDC hdc = NULL;
HPEN hpen = NULL;

void initgraph(int* gd, int* gm, char* path) {
    *gd = DETECT;
    *gm = 0;
}

void putpixel(int x, int y, int color) {
    cout << "Pixel at (" << x << ", " << y << ")" << endl;
}

void delay(int ms) {
    Sleep(ms);
}

void getch() {
    cin.get();
}

void closegraph() {
    if (hwnd) DestroyWindow(hwnd);
}

#endif
