/*****************************************************************************/
/*                                                                           */
/*                           mur0.c                                          */
/*                                                                           */
/*  Programa inicial d'exemple per a les practiques 2 de FSO.                */
/*                                                                           */
/*  Compilar i executar:                                                     */
/*     El programa invoca les funcions definides a "winsuport.c", les        */
/*     quals proporcionen una interficie senzilla per crear una finestra     */
/*     de text on es poden escriure caracters en posicions especifiques de   */
/*     la pantalla (basada en CURSES); per tant, el programa necessita ser   */
/*     compilat amb la llibreria 'curses':                                   */
/*                                                                           */
/*       $ gcc -Wall -c winsuport.c -o winsuport.o                           */
/*       $ gcc -Wall mur0.c winsuport.o -o mur0 -lcurses                     */
/*                                                                           */
/*  Al tenir una orientació vertical cal tenir un terminal amb prou files.   */
/*  Per exemple:                                                             */
/*               xterm -geometry 80x50                                       */
/*               gnome-terminal --geometry 80x50                             */
/*                                                                           */
/*****************************************************************************/

#include <stdint.h>		/* intptr_t for 64bits machines */
#include <stdio.h>		/* incloure definicions de funcions estandard */
#include <stdlib.h>
#include <string.h>
#include "winsuport2.h"		/* incloure definicions de funcions propies */
#include <pthread.h>
#include <unistd.h>
#include "memoria.h"
#include <sys/wait.h>

/* definicio de constants */
#define SIZE_ARRAY 32
#define MAX_THREADS	10
#define MAXBALLS	(MAX_THREADS-1)
#define MIN_FIL	10		/* dimensions del camp. Depenen del terminal ! */
#define MAX_FIL	50
#define MIN_COL	10
#define MAX_COL	80
#define BLKSIZE	3
#define BLKGAP	2
#define BLKCHAR 'B'
#define WLLCHAR 'B'
#define FRNTCHAR 'A'
#define LONGMISS	65

/* variables globals */
pid_t tpid[MAXBALLS];
int *c_pal, *f_pal, *nblocs, *num_pilotes, *dirPaleta, retard, ind, c_pil, f_pil, num_fills;
int m_pal;
int id_mem_tauler, n_fil, n_col;
int n_p, n_b;
float vel_f, vel_c, pos_f, pos_c;
int dir_p, c_p, f_p, *fi1, fi_1;

/* Si hi ha una col.lisió pilota-bloci esborra el bloc */
void comprovar_bloc(int f, int c)
{
	int col;
	char quin = win_quincar(f, c);

	if (quin == BLKCHAR || quin == FRNTCHAR) {
		col = c;
		while (win_quincar(f, col) != ' ') {
			win_escricar(f, col, ' ', NO_INV);
			col++;
		}
		col = c - 1;
		while (win_quincar(f, col) != ' ') {
			win_escricar(f, col, ' ', NO_INV);
			col--;
		}

		/* generar nova pilota ? */

		if (quin == BLKCHAR)
		{
			char id_str[SIZE_ARRAY], fil_str[SIZE_ARRAY], col_str[SIZE_ARRAY];
			char id_mem_tauler_str[SIZE_ARRAY], vel_f_str[SIZE_ARRAY], vel_c_str[SIZE_ARRAY];
			char f_pil_str[SIZE_ARRAY], c_pil_str[SIZE_ARRAY];
			char pos_f_str[SIZE_ARRAY], pos_c_str[SIZE_ARRAY];
			char nblocs_str[SIZE_ARRAY], npils_str[SIZE_ARRAY], retard_str[SIZE_ARRAY];
			char c_pal_str[SIZE_ARRAY], f_pal_str[SIZE_ARRAY], dirPaleta_str[SIZE_ARRAY], fi1_str[SIZE_ARRAY];
			
			tpid[num_fills] = fork();
			if (tpid[num_fills] == 0)   /* Es tracta del proces fill */
			{
				execlp("./pilota3", "pilota3", id_str, id_mem_tauler_str, fil_str,
					col_str, vel_f_str, vel_c_str, pos_f_str, pos_c_str, f_pil_str,
					c_pil_str, nblocs_str, npils_str, retard_str, c_pal_str, f_pal_str, dirPaleta_str, fi1_str, (char *)0);
		        fprintf(stderr, "Error: No puc executar el proces fill \'pilota3\' \n");
		        exit(1);  /* Retornem error */
			}
			(*num_pilotes)++;
			num_fills++;
		}
		(*nblocs)--;
	}
}

/* funcio per a calcular rudimentariament els efectes amb la pala */
/* no te en compta si el moviment de la paleta no és recent */
/* cal tenir en compta que després es calcula el rebot */
void control_impacte(void) {

	for (int i = 1; i <= *num_pilotes; i++){
		if (*dirPaleta == TEC_DRETA) {
			if (vel_c <= 0.0)	/* pilota cap a l'esquerra */
				vel_c = -vel_c - 0.2;	/* xoc: canvi de sentit i reduir velocitat */
			else {	/* a favor: incrementar velocitat */
				if (vel_c <= 0.8)
					vel_c += 0.2;
			}
		} else {
			if (*dirPaleta == TEC_ESQUER) {
				if (vel_c >= 0.0)	/* pilota cap a la dreta */
					vel_c = -vel_c + 0.2;	/* xoc: canvi de sentit i reduir la velocitat */
				else {	/* a favor: incrementar velocitat */
					if (vel_c >= -0.8)
						vel_c -= 0.2;
				}
			} else {	/* XXX trucs no documentats */
				if (*dirPaleta == TEC_AMUNT)
					vel_c = 0.0;	/* vertical */
				else {
					if (*dirPaleta == TEC_AVALL)
						if (vel_f <= 1.0)
							vel_f -= 0.2;	/* frenar */
				}
			}
		}
		(*dirPaleta)=0;	/* reset perque ja hem aplicat l'efecte */
	}

}

float control_impacte2(int c_pil, float velc0) {
	int distApal;
	float vel_c;

	distApal = c_pil - (intptr_t) *c_pal;
	if (distApal >= 2 * m_pal/3)	/* costat dreta */
		vel_c = 0.5;
	else if (distApal <= m_pal/3)	/* costat esquerra */
		vel_c = -0.5;
	else if (distApal == m_pal/2)	/* al centre */
		vel_c = 0.0;
	else /*: rebot normal */
		vel_c = velc0;
	return vel_c;
}

int main(int n_args, char *ll_args[])
{
	num_fills = 0;
	int fi2 = 0;
	int fi3 = 0;
	/* Parsing arguments */
	ind = atoi(ll_args[1]);
	id_mem_tauler = atoi(ll_args[2]);
	n_fil = atoi(ll_args[3]);
	n_col = atoi(ll_args[4]);
	vel_f = atof(ll_args[5]);
	vel_c = atof(ll_args[6]);
	pos_f = atof(ll_args[7]);
	pos_c = atof(ll_args[8]);
	f_pil = atoi(ll_args[9]);
	c_pil = atoi(ll_args[10]);
	n_b = atoi(ll_args[11]);
	n_p =  atoi(ll_args[12]);
	retard = atoi(ll_args[13]);
	c_p = atoi(ll_args[14]);
	f_p = atoi(ll_args[15]);
	dir_p = atoi(ll_args[16]);
	fi_1 = atoi(ll_args[17]);
	
    void * addr_tauler = map_mem(id_mem_tauler);
    win_set(addr_tauler, n_fil, n_col);
   
	num_pilotes = map_mem(n_p);
	nblocs = map_mem(n_b);
	c_pal = map_mem(c_p);
	f_pal = map_mem(f_p);
	dirPaleta = map_mem(dir_p);
	fi1 = map_mem(fi_1);


	int f_h, c_h;
	char rh, rv, rd;
	do {
		f_h = pos_f + vel_f;	/* posicio hipotetica de la pilota (entera) */
		c_h = pos_c + vel_c;
		rh = rv = rd = ' ';
		if ((f_h != f_pil) || (c_h != c_pil)) {
		/* si posicio hipotetica no coincideix amb la posicio actual */
			if (f_h != f_pil) {	/* provar rebot vertical */
				rv = win_quincar(f_h, c_pil);	/* veure si hi ha algun obstacle */
				if (rv != ' ') {	/* si hi ha alguna cosa */
					comprovar_bloc(f_h, c_pil);
					if (rv == '0')	/* col.lisió amb la paleta? */
	//					control_impacte();
						vel_c = control_impacte2(c_pil, vel_c);
					vel_f = -vel_f;	/* canvia sentit velocitat vertical */
					f_h = pos_f + vel_f;	/* actualitza posicio hipotetica */
				}
			}
			if (c_h != c_pil) {	/* provar rebot horitzontal */
				rh = win_quincar(f_pil, c_h);	/* veure si hi ha algun obstacle */
				if (rh != ' ') {	/* si hi ha algun obstacle */
					comprovar_bloc(f_pil, c_h);
					/* TODO?: tractar la col.lisio lateral amb la paleta */
					vel_c = -vel_c;	/* canvia sentit vel. horitzontal */
					c_h = pos_c + vel_c;	/* actualitza posicio hipotetica */
				}
			}
			if ((f_h != f_pil) && (c_h != c_pil)) {	/* provar rebot diagonal */
				rd = win_quincar(f_h, c_h);
				if (rd != ' ') {	/* si hi ha obstacle */
					comprovar_bloc(f_h, c_h);
					vel_f = -vel_f;
					vel_c = -vel_c;	/* canvia sentit velocitats */
					f_h = pos_f + vel_f;
					c_h = pos_c + vel_c;	/* actualitza posicio entera */
				}
			}
			/* mostrar la pilota a la nova posició */
			if (win_quincar(f_h, c_h) == ' ') {	/* verificar posicio definitiva *//* si no hi ha obstacle */
				win_escricar(f_pil, c_pil, ' ', NO_INV);	/* esborra pilota */
				pos_f += vel_f;
				pos_c += vel_c;
				f_pil = f_h;
				c_pil = c_h;	/* actualitza posicio actual */
				if (f_pil != n_fil - 1){	/* si no surt del taulell, */
					win_escricar(f_pil, c_pil, '1', INVERS);	/* imprimeix pilota */
				}
				else{
					(*num_pilotes)--;
					fi3 = 1;
				}
			}
		} 
		else {	/* posicio hipotetica = a la real: moure */
			pos_f += vel_f;
			pos_c += vel_c;
		}
		win_retard(retard);
	} while (!(*fi1) && !fi2 && !fi3);	
	int i;
	int stat;
	for (i=0; i <= num_fills; i++){
		waitpid(tpid[i], &stat, 0);
	}
	
	return (fi3);
}

