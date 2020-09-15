#include <stdio.h>
int sum(int *pa,int ne){
	int s=0;
	for (int i=0;i<ne;i++)
		s+=*(pa+i);
	printf ("%d",s);
	return s;
}
void vvod (int *pa,int ne){
	printf ("Vvedite massiv iz %d chisel:",ne);
	for (int i=0;i<ne;i++)
		scanf ("%d",(pa+i));
}
int main (){
	int a[10],n;
	scanf ("%d",&n);
	vvod (a,n);
	sum (a,n);
	return 0;

}