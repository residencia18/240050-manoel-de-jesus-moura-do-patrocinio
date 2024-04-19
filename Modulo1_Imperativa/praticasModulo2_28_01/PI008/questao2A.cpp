#include <iostream>

using namespace std;

int main(void)
{
    int arr[20], arr2[20], vezesRepetidas = 0, MaisRepetido;

    for (int i = 0; i < 20; i++)
    {
        arr[i] = 1 + (rand() % 20);
    }
    for (int i = 0; i < 20; i++)
    {
        cout << arr[i] << " ";
    }

    cout << endl;
    cout << endl;

    for (int i = 0; i < 20; i++)
    {
        int contador = 0;
        int repetiu = false;

        for (int z = 0; z < sizeof(arr2); z++)
        {
            if (arr2[z] == arr[i])
            {
                repetiu = true;
            }
        }
        if (repetiu == false)
        {
            arr2[i] = arr[i]; // add no  array auxiliar que este número vai ser verificado
            for (int j = 0; j < 20; j++)
            {
                if (arr[i] == arr[j])
                {
                    contador++;
                }
            }
            cout << "O número: " << arr[i] << " repetiu: " << contador << " vezes" << endl;

            if (vezesRepetidas < contador)
            {
                vezesRepetidas = contador;
                MaisRepetido = arr[i];
            }
        }
    }
    cout << "O número que mais se repetiu foi o: " << MaisRepetido << endl;

    return 0;
}