

double f(int n, doouble a[], double x)
{
    int i;
    double p=a[0];
    for(i=1;i<=n;i++)
        p+=(a[i]*pow(x,i));
    return p;
}


double f(int n, double a[], double x)
{
    int i;
    double p=a[n];
    for(i=n;i>0;i--)
        p=a[i-1]+x*p;
    return p;

}
