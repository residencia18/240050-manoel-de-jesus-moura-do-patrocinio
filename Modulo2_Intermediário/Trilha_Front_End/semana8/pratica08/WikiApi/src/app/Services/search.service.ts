import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { WikipediaPage } from '../types/reponseWikipedia';

import { catchError, map } from 'rxjs/operators';
@Injectable({
  providedIn: 'root'
})
export class SearchService {

  private apiUrl = '/wikipedia-api/w/api.php';
  private pageContent: WikipediaPage | undefined;

  constructor(private http: HttpClient) { }

  search(title: string): Observable<WikipediaPage> {
    const params = {
      action: 'parse',
      page: title,
      format: 'json'
    };

    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
    });

    return this.http.get<WikipediaPage>(`${this.apiUrl}`, { params, headers, responseType: 'text' as 'json' })
        
      
  }
  setRearchData(data:WikipediaPage){
    this.pageContent = data;

  }
  getWikiData(): Observable<WikipediaPage | undefined> {
    return new Observable(observer => {
      if (this.pageContent) {
        observer.next(this.pageContent);
      }
    });
  }


}
