import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { GetPaisesService } from '../../services/get-paises.service';
import { CommonModule, NgFor, NgIf, TitleCasePipe } from '@angular/common';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [ReactiveFormsModule,NgFor,NgIf,TitleCasePipe,CommonModule,HttpClientModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css',
  providers: [GetPaisesService]
})
export class HomeComponent {
  camposChaves: string[] = []
  form: FormGroup = new FormGroup({});

  constructor(private http: HttpClient, private paisesService: GetPaisesService, private formBuilder: FormBuilder) { }

  ngOnInit() {
    this.paisesService.getPaises().subscribe(res => {
      this.camposChaves = res
      console.log("resposta", res)
      this.createForm()

    })
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
