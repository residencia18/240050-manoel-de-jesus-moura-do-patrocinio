import { Component } from '@angular/core';
import { CommonModule, NgFor, NgIf, TitleCasePipe } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, HttpClientModule, ReactiveFormsModule, NgFor, NgIf, TitleCasePipe],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'feb06';
  camposChaves: string[] = []
  form: FormGroup = new FormGroup({});

  constructor(private http: HttpClient, private formBuilder: FormBuilder) { }

  ngOnInit() {
    this.http.get<any>(`https://restcountries.com/v3.1/all`).subscribe(
      resData => {
        // console.log('API response data: ', resData[0].name );
        this.camposChaves = resData ? Object.keys(resData[0].name) : [];
        this.camposChaves.push('capital', 'region')
        console.log('compos extraídos: ', this.camposChaves);
        this.createForm()
      }
    )
  }

  createForm() {
    const formControls: any = {};
    this.camposChaves.forEach(field => {
      formControls[field] = ['', Validators.required];
    });
    this.form = this.formBuilder.group(formControls);
  }

  onSubmit() {
    if (this.form.valid) {
      alert("Cadastrado com sucesso")
      console.log(this.form.value);
      this.form.reset()
      window.location.reload()
    } else {
      alert("Preencha todos os dados corretamente");
    }
  }

}
