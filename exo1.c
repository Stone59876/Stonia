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
    printf("Voici la somme %i et la moyenne %f \n",som,moy);
    return 0;
}

int exo6()
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

int exo7()
{
    float val;
    int estZero;
    float max;
    float f;
    max = 0;
    estZero = 0;
    val = 0;
    printf("Entrez une valeur : \n");
    scanf("%f",&f);
    val = f;
    max = val;
    while (estZero == 0)
    {
    printf("Entrez une valeur : \n");
    scanf("%f",&f);
    if (f == 0)
        estZero = 1;
    else
        if (f > max)
            max = f;
    }
    printf("Le maximum est %f",max);
    return 0;
}

int exo8()
{
    float val;
    int estZero;
    float som;
    float f;
    int compt;
    float moy;
    moy = 0;
    compt = 1;
    som = 0;
    estZero = 0;
    val = 0;
    printf("Entrez une valeur : \n");
    scanf("%f",&f);
    val = f;
    som = som + val;
    while (estZero == 0)
    {
    printf("Entrez une valeur : \n");
    scanf("%f",&f);
    if (f == 0)
        estZero = 1;
    else
        {
          compt = compt + 1;
          val = f;
          som = som + val;
        }
    }
    moy = som / compt;
    printf("La moyenne est %f",moy);
    return 0;
}

int exo9()
{
    float val;
    int posmax;
    int estZero;
    float max;
    float f;
    int compteur;
    compteur = 1;
    posmax = 1;
    max = 0;
    estZero = 0;
    val = 0;
    printf("Entrez une valeur : \n");
    scanf("%f",&f);
    val = f;
    max = val;
    while (estZero == 0)
    {
    printf("Entrez une valeur : \n");
    scanf("%f",&f);
    if (f == 0)
        estZero = 1;
    else
        {
        compteur = compteur + 1;
        if (f > max)
            {
            max = f;
            posmax = compteur;
            }
        }
    }
    printf("Le maximum est %f a la position %i",max,posmax);
    return 0;
}

int exo10()
{
    int salaireHoraire;
    int heureDeTravail;
    int salaireTotal;
    int heureSup;
    int heureMegaSup;
    heureSup = 0;
    heureMegaSup = 0;
    salaireTotal = 0;
    printf("Quel est le salaire horaire ? \n");
    scanf("%i",&salaireHoraire);
    printf("Combien d'heure de travail ? \n");
    scanf("%i",&heureDeTravail);
    if (heureDeTravail <= 35)
        salaireTotal = heureDeTravail*salaireHoraire;
    else
        {
        if(heureDeTravail <= 45)
            {
            heureSup = heureDeTravail - 35;
            salaireTotal = (35 * salaireHoraire) + (heureSup * salaireHoraire * 1.5);
            }
        else
            {
            heureMegaSup = heureDeTravail - 45;
            salaireTotal = (35 * salaireHoraire) + (10 * salaireHoraire * 1.5) + (heureMegaSup * salaireHoraire * 1.75);
            }
        }
    printf("Le salaire total du salarie est de %i",salaireTotal);
    return 0;
}

int exo11()
{
    int multiple;
    int n;
    int m;
    int val;
    val = 0;
    printf("Entrez la valeur de n: \n");
    scanf("%i",&n);
    printf("Entrez la valeur de m: \n");
    scanf("%i",&m);
    for (multiple = 1 ; multiple < n ; multiple++)
    {
        val = multiple * m;
        printf("%i fois %i est egale a %i \n",multiple,m,val);
    }
    return 0;
}

int exo12()
{
    int estZero;
    int n1;
    int n2;
    int DernierestN1;
    int compteur;
    int val;
    estZero = 0;
    compteur = 0;
    DernierestN1 = 0;
    printf("Entrez la valeur de n1: \n");
    scanf("%i",&n1);
    printf("Entrez la valeur de n2: \n");
    scanf("%i",&n2);
    printf("Entrez votre suite de valeur : \n");
    scanf("%i",&val);
    while (estZero == 0)
    {
    printf("Entrez votre valeur : \n");
    scanf("%i",&val);
        if (val == 0)
        {
            estZero = 1;
        }
        else
        {
            if(DernierestN1 == 1 && val == n2)
            {
                compteur = compteur + 1;
            }
            else
            {
                if (val == n1)
                {
                    DernierestN1 = 1;
                }
                else
                {
                    DernierestN1 = 0;
                }
            }
        }
    }
    printf("Il y a eu %i suivi de %i dans cette suite %i fois",n1,n2,compteur);
    return 0;
}
