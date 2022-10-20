%option noyywrap
%{
  #include <stdio.h>
  int option = 0;
  float a, b;
  void digi();
%}
  
dig [0-9]+|([0-9]*)"."([0-9]+)
addition "+"
subtraction "-"
multiplication "*"
division "/"

power_of_number "^"
modular "%"
square_root "rt"
logarithm "lg"
natural_logarithm "ln"

result \n

%%
{dig} {digi();} 
{addition} {option=1;}
{subtraction} {option=2;}
{multiplication} {option=3;}
{division} {option=4;}
{power_of_number} {option=5;}
{modular} {option=6;}
{square_root} {option=7;}
{logarithm} {option=8;}
{natural_logarithm} {option=9;}

[\n] {
printf("\n The Answer :%f\n\n",a);
}
  
%%

void digi()
{
 if(option==0)
  
 a=atof(yytext); 
  
 else
 {
 b=atof(yytext);
  
 switch(option)
 {
   case 1:
   a=a+b;
   break;
  
   case 2:
   a=a-b;
   break;
   
   case 3:
   a=a*b;
   break;
   
   case 4:
   a=a/b;
   break;
   
   case 5:
   a = pow(a,b);
   break;
   
   case 6:
   while (a >= b)
   {
   a -= b;
   }
   res = a;
   break;
   
   case 7:
   a=pow(a,(1/b));
   break;
   
   case 8:
   a=log(a)/log(b);
   break;
   
   case 9:
   a=log(a);
   break; 
   
  }
 option=0;
 }
}
  
int main(void)
{
 yylex();
 return 0;
}

