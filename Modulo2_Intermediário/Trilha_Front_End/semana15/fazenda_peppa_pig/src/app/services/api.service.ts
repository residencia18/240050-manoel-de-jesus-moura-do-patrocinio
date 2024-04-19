import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable, catchError, map, tap, throwError } from 'rxjs';
import Swal from 'sweetalert2';
import { type_suino, type_suino_peso } from '../types/type_suino';
import { type_sessao } from '../types/type_sessao';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }

  cadastroSuino(newSuinoData: type_suino) {

    return this.http.post(
      'https://residencia-b1914-default-rtdb.firebaseio.com/suinos.json',
      newSuinoData)
      .pipe(
        tap(resData => {
          return resData
        }),
        catchError(error => {
          console.error(error);
          Swal.fire({
            icon: 'error',
            title: 'Erro!',
            text: 'Ocorreu um erro no cadastro do suíno. Por favor, tente novamente.'
          });
          return throwError(error);
        })
      )

  }
  getListaSuinos() {

    return this.http.get<{ [key: string]: type_suino }>('https://residencia-b1914-default-rtdb.firebaseio.com/suinos.json',
      {
        params: new HttpParams().set('print', 'pretty')
      }
    ).pipe(
      catchError(error => {
        console.error(error);
        Swal.fire({
          icon: 'error',
          title: 'Erro!',
          text: 'Ocorreu um erro ao buscar lista de suínos. Por favor, tente novamente.'
        });
        return throwError(error);
      }),
      map(responseData => {
        // Convertendo o objeto de resposta em um array de objetos
        if (responseData) {
          return Object.keys(responseData).map(key => ({ id: key, ...responseData[key] }));
        } else {
          return [];
        }
      })
    )

  }
  getSuinoById(suino_id: string) {

    return this.http.get<type_suino>(`https://residencia-b1914-default-rtdb.firebaseio.com/suinos/${suino_id}.json`,
      {
        params: new HttpParams().set('print', 'pretty')
      }
    ).pipe(
      catchError(error => {
        console.error(error);
        Swal.fire({
          icon: 'error',
          title: 'Erro!',
          text: 'Ocorreu um erro ao buscar o atendimento. Por favor, tente novamente.'
        });
        return throwError(error);
      })
    )

  }

  apagarTodaListaSuino() {
    return this.http.delete('https://residencia-b1914-default-rtdb.firebaseio.com/suinos.json');
  }

  deleteSuinoById(suino_id: string) {
    const url = `https://residencia-b1914-default-rtdb.firebaseio.com/suinos/${suino_id}.json`;
    this.http.delete(url).pipe(
      catchError(error => {
        console.error(error);
        Swal.fire({
          icon: 'error',
          title: 'Erro!',
          text: 'Ocorreu um erro ao exlcuir o atendimento. Por favor, tente novamente.'
        });
        return throwError(error);
      })
    ).subscribe(responseData => {
      Swal.fire({
        icon: 'success',
        title: 'Sucesso!',
        text: 'Atendimento excluído com sucesso.',
        timer: 2500,
        showConfirmButton: false,

      });
      setTimeout(() => {

        window.location.reload()
      }, 3000)
    });
  }


  editarSuino(id: string, newSuinoData: any) {
    return this.http.put(`https://residencia-b1914-default-rtdb.firebaseio.com/suinos/${id}.json`, newSuinoData, { observe: 'response' })
      .pipe(
        catchError(error => {
          console.error(error);
          Swal.fire({
            icon: 'error',
            title: 'Erro!',
            text: 'Ocorreu um erro ao editar o atendimento. Por favor, tente novamente.'
          });
          return throwError(error);
        })
      )
  }

  // LOGICA PARA PESOS


  cadastroPesoSuino(newSuinoData: any) {

    return this.http.post<type_suino_peso>(
      'https://residencia-b1914-default-rtdb.firebaseio.com/suinoPeso.json',
      newSuinoData)
      .pipe(
        catchError(error => {
          console.error(error);
          Swal.fire({
            icon: 'error',
            title: 'Erro!',
            text: 'Ocorreu um erro ao adicionar o atendimento. Por favor, tente novamente.'
          });
          return throwError(error);
        })
      )
  }

  getListPesoSuinos() {

    return this.http.get<{ [key: string]: type_suino_peso }>(`https://residencia-b1914-default-rtdb.firebaseio.com/suinoPeso.json`,
      {
        params: new HttpParams().set('print', 'pretty')
      }
    ).pipe(
      catchError(error => {
        console.error(error);
        Swal.fire({
          icon: 'error',
          title: 'Erro!',
          text: 'Ocorreu um erro ao buscar histórico de pesos. Por favor, tente novamente.'
        });
        return throwError(error);
      }),
      map(responseData => {
        // Convertendo o objeto de resposta em um array de objetos
        if (responseData) {
          return Object.keys(responseData).map(key => ({ id: key, ...responseData[key] }));
        } else {
          return [];
        }

      })
    )

  }

  getPesoSuinoById(suinoId:string) {

    return this.http.get< type_suino_peso >(`https://residencia-b1914-default-rtdb.firebaseio.com/suinoPeso/${suinoId}.json`,
      {
        params: new HttpParams().set('print', 'pretty')
      }
    ).pipe(
      catchError(error => {
        console.error(error);
        Swal.fire({
          icon: 'error',
          title: 'Erro!',
          text: 'Ocorreu um erro ao buscar peso do suino por id. Por favor, tente novamente.'
        });
        return throwError(error);
      }),
      
    )

  }

  
  deletePesoSuinoById(suino_id: string) {
    const url = `https://residencia-b1914-default-rtdb.firebaseio.com/suinoPeso/${suino_id}.json`;
    this.http.delete(url).pipe(
      catchError(error => {
        console.error(error);
        Swal.fire({
          icon: 'error',
          title: 'Erro!',
          text: 'Ocorreu um erro ao exlcuir o atendimento. Por favor, tente novamente.'
        });
        return throwError(error);
      })
    ).subscribe(responseData => {
      Swal.fire({
        icon: 'success',
        title: 'Sucesso!',
        text: 'Atendimento excluído com sucesso.',
        timer: 2500,
        showConfirmButton: false,

      });
      setTimeout(() => {

        window.location.reload()
      }, 3000)
    });
  }

  editarPesoSuino(id: string, newSuinoData: any) {
    return this.http.put(`https://residencia-b1914-default-rtdb.firebaseio.com/suinoPeso/${id}.json`, newSuinoData, { observe: 'response' })
      .pipe(
        catchError(error => {
          console.error(error);
          Swal.fire({
            icon: 'error',
            title: 'Erro!',
            text: 'Ocorreu um erro ao editar o atendimento. Por favor, tente novamente.'
          });
          return throwError(error);
        })
      )
  }

  // LÓGICA PARA SESSÃO
  cadastroSessao(newSection: any) {

    return this.http.post(
      'https://residencia-b1914-default-rtdb.firebaseio.com/sessao.json',
      newSection)
      .pipe(
        tap(resData => {
          return resData
        }),
        catchError(error => {
          console.error(error);
          Swal.fire({
            icon: 'error',
            title: 'Erro!',
            text: 'Ocorreu um erro no cadastro da sessão. Por favor, tente novamente.'
          });
          return throwError(error);
        })
      )

  }

  getListSessoes() {

    return this.http.get<{ [key: string]: type_sessao }>(`https://residencia-b1914-default-rtdb.firebaseio.com/sessao.json`,
      {
        params: new HttpParams().set('print', 'pretty')
      }
    ).pipe(
      catchError(error => {
        console.error(error);
        Swal.fire({
          icon: 'error',
          title: 'Erro!',
          text: 'Ocorreu um erro ao buscar a lista de sessões. Por favor, tente novamente.'
        });
        return throwError(error);
      }),
      map(responseData => {
        // Convertendo o objeto de resposta em um array de objetos
        if (responseData) {
          return Object.keys(responseData).map(key => ({ id: key, ...responseData[key] }));
        } else {
          return [];
        }

      })
    )

  }


}
