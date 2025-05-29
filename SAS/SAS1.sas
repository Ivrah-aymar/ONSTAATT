/***SAS Program structure: DATA , PROC, OUTPUT
Data create a data set – source for analysis, PROC – to analyze, OUTPUT to show/store results
DATA, INPUT, LABEL, DATALINES, RUN ***/
/**example1  **/ /*** "**comment**" doesnt work **/
DATA TEMPDS;
INPUT ID NAME $ SALARY DEPARTMENT $;
/***EXTDAY;***/
/***SAL_EXT=SALARY*0.033*EXTDAY ***/
LABEL ID=“EMP ID” SAL_EXT=‘EXTRA HOURS PAY’;
DATALINES;
301 ABC 9500 RSA 
302 EFG 6500 DGT 
303 HIG 3200 DBT 
304 TGH 5600 ITI  
/** ; in 304 line gave error/warning **/
;
RUN;
/*** MEANS to get mean of numeric var values***/
PROC MEANS;
RUN;
/***output -- **/
PROC PRINT DATA=TEMPDS;
RUN;

/*** output
The MEANS Procedure
Variable	Label	N	Mean	Std Dev	Minimum	Maximum
ID        "EMP ID"
 
Obs	ID	NAME	SALARY	DEPARTMENT
1	301	ABC	9500	RSA
2	302	EFG	6500	DGT
3	303	HIG	3200	DBT
4	304	TGH	5600	ITI

***/
