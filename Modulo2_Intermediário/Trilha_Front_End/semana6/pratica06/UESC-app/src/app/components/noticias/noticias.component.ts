import { NgFor, NgIf } from '@angular/common';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Component } from '@angular/core';

interface IapiNoticesResponse {
  status: string,
  totalHits: number,
  data: Article[]
}
interface Article {
  id: string;
  authors: string[];
  contributors: string[];
  description: string;
  identifiers: string[];
  publisher: string;
  relations: any[];
  repositories: string[];
  repositoryDocument: {
    [key: string]: any;
  };
  subjects: string[];
  title: string;
  topics: string[];
  types: any[];
  year: number;
  fulltextIdentifier: string;
  oai: string;
  downloadUrl: string;
}

@Component({
  selector: 'app-noticias',
  standalone: true,
  imports: [NgFor, NgIf],
  templateUrl: './noticias.component.html',
  styleUrl: './noticias.component.css'
})


export class NoticiasComponent {
  noticias: Article[] = [];
  apiKey: string = '9Xzyk6QRlWpuKdarLe0ZUgPSbq2cn48o';
  searchTerm: string = 'machine learning';
  error: string | null = null;


  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.http.get<IapiNoticesResponse>(`https://core.ac.uk/api-v2/articles/search/${this.searchTerm}?apiKey=${this.apiKey}`)
      .subscribe({
        next: (data: IapiNoticesResponse) => {
          this.noticias = data.data;
        },
        error: (error: HttpErrorResponse) => {
          this.error = error.message;
        }
      });

  }
}
