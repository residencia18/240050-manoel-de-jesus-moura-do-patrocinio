import { Component } from '@angular/core';
import { AbstractControl, FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { type_suino } from '../../types/type_suino';
import { ApiService } from '../../services/api.service';
import { ActivatedRoute, Router } from '@angular/router';
import Swal from 'sweetalert2';
import { NgFor, NgIf } from '@angular/common';

@Component({
  selector: 'app-edicao-suino',
  standalone: true,
  imports: [ReactiveFormsModule,NgIf,NgFor],
  templateUrl: './edicao-suino.component.html',
  styleUrl: './edicao-suino.component.css'
})
export class EdicaoSuinoComponent {

  SuinoEditForm: FormGroup = new FormGroup({});
  suinoId: string = ""
  suinaData: type_suino | null = null

  constructor(private apiService: ApiService, private formBuilder: FormBuilder, private rotas: Router, private rota: ActivatedRoute) { }

  ngOnInit(): void {
    this.suinoId = this.rota.snapshot.params['id']
    this.SuinoEditForm = this.formBuilder.group({
      'Brinco': [null, [Validators.required]],
      'BrincoPai': [null, [Validators.required]],
      'BrincoMae': [null, [Validators.required]],
      'DataNascimento': [null, [Validators.required, this.validateDataMaior.bind(this)]],
      'DataSaida': [null, [Validators.required]],
      'Status': [null, [Validators.required]],
      'Sexo': [null, [Validators.required]],

    })


    this.apiService.getSuinoById(this.suinoId).subscribe((response) => {
      this.suinaData = response;
    })

    setTimeout(() => {
      this.setFormValues()
    }, 1000)

  }

  validateDataMaior(control: AbstractControl) {
    const DataNascimento = new Date(control.value);
    const currentDate = new Date();

    if (!DataNascimento || isNaN(DataNascimento.getTime())) {
      return { invalidDate: true };
    }

    if (DataNascimento > currentDate) {
      console.log("maior")
      return { invalidDate: true };
    }
    return null;
  }

  setFormValues() {
    console.log("this.suinaData", this.suinaData)

    if (this.suinaData !== null) {
      this.SuinoEditForm.setValue(this.suinaData);

    }

  }

  onSubmit(form: FormGroup) {
    if (this.SuinoEditForm.valid) {

      console.log("form.value",form.value)
      this.apiService.editarSuino(this.suinoId, form.value).subscribe(responseData => {
        Swal.fire({
          icon: 'success',
          title: 'Sucesso!',
          text: 'Atualizado com sucesso.',
          timer: 2000,
          showConfirmButton: false,
        });
        setTimeout(() => {
          this.SuinoEditForm.reset()
          this.rotas.navigate([`/list-suino`])

        }, 2500)
      });
    }
  }
}
