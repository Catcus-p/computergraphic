#include <iostream>
#include <cmath>
#include "graphics.h"

using namespace std;

int DDA(int x1, int y1, int x2, int y2) {
    int dx = x2 - x1;
    int dy = y2 - y1;
    int steps = (abs(dx) > abs(dy)) ? abs(dx) : abs(dy);

    float xinc = (float)dx / steps;
    float yinc = (float)dy / steps;

    float x = x1;
    float y = y1;

    putpixel(x, y, BLUE);

    for (int k = 0; k < steps; k++) {
        x += xinc;
        y += yinc;
        putpixel((int)(x + 0.5), (int)(y + 0.5), WHITE);
        delay(10);
    }
    
    return 0;
}

int main() {
    int gd = DETECT, gm = 0;
    initgraph(&gd, &gm, (char*)"");
    
    int x1, y1, x2, y2;
    
    cout << "=== DDA Line Drawing Algorithm ===" << endl;
    cout << "Enter x1 and y1: ";
    cin >> x1 >> y1;

    cout << "Enter x2 and y2: ";
    cin >> x2 >> y2;

    DDA(x1, y1, x2, y2);

    cout << "\nPress Enter to exit...";
    getch();
    closegraph();
    
    return 0;
}
