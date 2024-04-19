import { Component } from '@angular/core';
import { CommonModule, NgFor, NgIf, TitleCasePipe } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { GetPaisesService } from './services/get-paises.service'

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, HttpClientModule, ReactiveFormsModule, NgFor, NgIf, TitleCasePipe],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [GetPaisesService]
})
export class AppComponent {
  title = 'feb06';
  camposChaves: string[] = []
  form: FormGroup = new FormGroup({});

  constructor(private http: HttpClient) { }

  ngOnInit() {
    // this.http.get<any>(`https://restcountries.com/v3.1/all`).subscribe(
    //   resData => {
    //     // console.log('API response data: ', resData[0].name );
    //     this.camposChaves = resData ? Object.keys(resData[0].name) : [];
    //     this.camposChaves.push('capital', 'region')
    //     console.log('compos extraídos: ', this.camposChaves);
    //     this.createForm()
    //   }
    // )

  }

}
