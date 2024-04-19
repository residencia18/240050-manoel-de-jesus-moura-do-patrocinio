import { NgFor, NgIf } from '@angular/common';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
  selector: 'app-servicos',
  standalone: true,
  imports: [NgFor, NgIf],
  templateUrl: './servicos.component.html',
  styleUrl: './servicos.component.css'
})
export class ServicosComponent {
  apiKey: string = '519470a7867522f9b463c4e5b01fd0b3';
  cidade: string = 'Itabuna';
  response: any;
  error: string | null = null;

  constructor(private http: HttpClient) { }

  async ngOnInit() {

    this.http.get(`https://api.openweathermap.org/data/2.5/weather?q=${this.cidade},BR&appid=${this.apiKey}&units=metric`)
      .subscribe({
        next: (data) => {
          this.response = data;
        },
        error: (error: HttpErrorResponse) => {
          this.error = error.message;
        }
      });


  }
}
