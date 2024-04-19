import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { catchError, map, Observable, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GetPaisesService {

  constructor(private http: HttpClient) { }

  getPaises() {
    let camposChaves: string[] = []

    return this.http.get<{ [key: string]: any }>('https://restcountries.com/v3.1/all',
      {
        params: new HttpParams().set('print', 'pretty')
      }
    ).pipe(
      catchError(error => {
        console.error("service error",error);
        return throwError(error);
      }),
      map(responseData => {
        // Convertendo o objeto de resposta em um array de objetos
        if (responseData) {
          camposChaves = responseData ? Object.keys(responseData[0].name) : [];
          camposChaves.push('capital', 'region')
          console.log('compos extraídos: ', camposChaves);
          return camposChaves
        } else {
          return [];
        }
      })
    )

  }
}

