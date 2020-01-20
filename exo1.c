#include <stdio.h>
#include <stdlib.h>


int exo1()
{
    float a;
    printf("Entrez un reel: \n");
    scanf("%f",&a);
    if (a > 0)
        printf("Nombre Positif \n");
    else
        printf("Nombre Nul ou Negatif \n");
    return 0;
}

int exo2()
{
    float b;
    b = 7;
    if (b > 0)
        printf("Nombre Positif \n");
    else
        printf("Nombre Negatif ou Nul \n");
    return 0;
}


int exo3()
{
    int nb1;
    int nb2;
    int c;
    c = 0;
    nb1 = 17;
    nb2 = 15;
    if (nb1 > nb2)
    {
        c = nb2;
        nb2 = nb1;
        nb1 = c;
    }
    else
    {
        nb1 = nb1;
        nb2 = nb2;
    }
    printf("%i plus petit que %i \n",nb1,nb2);
    return 0;
}

int exo4()
{
    int nb1;
    int nb2;
    nb1 = 18;
    nb2 = 15;
    if (nb1 > nb2)
    {
        printf("%i est plus grand que %i",nb1,nb2);
    }
    else
    {
        printf("%i est plus grand que %i",nb2,nb1);
    }
    return 0;
}

int exo5()
{
    int n;
    int compteur;
    int som;
    int i;
    float moy;
    n = 5;
    compteur = 0;
    som = 0;
    moy = 0;
    i = 0;
    while (compteur < n)
    {
        printf("Entrez une valeur : \n");
        scanf("%i",&i);
        som = som + i;
        compteur = compteur + 1;
    }
    moy = som / n;
    printf("Voici la moyenne %f \n",moy);
    return 0;
}
