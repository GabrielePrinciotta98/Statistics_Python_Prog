#include <stdio.h>
#include <string.h>

#define N 7000
#define file "qualita_aria"

int main(void)
{
    char testo[N];
    FILE *fp = fopen(file, "r");
    int k = 0;
    char ch;
    while ((ch = getc(fp)) != -1)
    {
        testo[k] = ch;
        k++;
    }
    testo[k] = '\0';
    //printf("<%s>\n", testo);//Tracking

    int i;
    int j;
    int c = 0;
    for (i = 0; i< strlen(testo); i++)
    {
        if(testo[i] == 32)
        {
            if(testo[i+1] == 32)
            {
                j = i + 1;
                while(testo[j] == 32)
                {
                    c++;
                    j++;
                }
                printf(",");
                i += c;
                c = 0;
            }
            else
            {
                printf("%c", testo[i]);
            }
            continue;
        }
        printf("%c", testo[i]);
    }
    //printf("\n");


    return 0;
}
