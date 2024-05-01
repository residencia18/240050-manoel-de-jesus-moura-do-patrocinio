import { Injectable } from '@angular/core';
import { type_atendimento } from '../types/atendimento';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable, catchError, map, throwError } from 'rxjs';
import Swal from 'sweetalert2';
import { type_api_returnAllProducts, type_product } from '../types/product';

@Injectable({
  providedIn: 'root'
})
export class ApiService {



  constructor(private http: HttpClient) { }



  addAtendimento(newAtendimento: type_atendimento) {

    this.http.post(
      'https://residencia-b1914-default-rtdb.firebaseio.com/posts.json',
      newAtendimento)
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
      ).subscribe(responseData => {
        console.log(responseData);
        Swal.fire({
          icon: 'success',
          title: 'Sucesso!',
          text: 'Atendimento adicionado com sucesso.',
          timer:2500,
          showConfirmButton: false,
        });
      });
  }

  

  getAtendimento() {

    return this.http.get< {[key:string]: type_atendimento}>('https://residencia-b1914-default-rtdb.firebaseio.com/posts.json',
      {
        params: new HttpParams().set('print', 'pretty')
      }
    ).pipe(
      catchError( error =>{
        console.error(error);
        Swal.fire({
          icon: 'error',
          title: 'Erro!',
          text: 'Ocorreu um erro ao buscar os atendimentos. Por favor, tente novamente.'
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



  getAtendimentoById(atend_id:string) {

    return this.http.get< type_atendimento>(`https://residencia-b1914-default-rtdb.firebaseio.com/posts/${atend_id}.json`,
      {
        params: new HttpParams().set('print', 'pretty')
      }
    ).pipe(
      catchError( error =>{
        console.error(error);
        Swal.fire({
          icon: 'error',
          title: 'Erro!',
          text: 'Ocorreu um erro ao buscar o atendimento. Por favor, tente novamente.'
        });
        return throwError(error);
      }),
      map(responseData => {
        // Convertendo o objeto de resposta em um array de objetos

          return responseData as type_atendimento;
   
      })
    )

  }




  apagarTodosAtendimentos() {
    return this.http.delete('https://residencia-b1914-default-rtdb.firebaseio.com/posts.json');
  }

  apagarAtendimentoById(atendimentoId: string){
    const url = `https://residencia-b1914-default-rtdb.firebaseio.com/posts/${atendimentoId}.json`;
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
        timer:2500,
        showConfirmButton: false,

      });
      setTimeout(()=>{

        window.location.reload()
      }, 3000)
    });
  }

  
  editarAtendimento(id:string, newAtendimento: type_atendimento) {
    return this.http.put(`https://residencia-b1914-default-rtdb.firebaseio.com/posts/${id}.json`, newAtendimento, {observe: 'response'})
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
    ).subscribe(responseData => {
      console.log(responseData);
      Swal.fire({
        icon: 'success',
        title: 'Sucesso!',
        text: 'Atendimento editado com sucesso.',
        timer:2500,
        showConfirmButton: false,
      });
    });
  }

  // LOGIC TO PRODUCTS

  getAllProducts():Observable<type_api_returnAllProducts> {
    return this.http.get< type_api_returnAllProducts>(`https://petfood-backend.onrender.com/`)
  }
}
