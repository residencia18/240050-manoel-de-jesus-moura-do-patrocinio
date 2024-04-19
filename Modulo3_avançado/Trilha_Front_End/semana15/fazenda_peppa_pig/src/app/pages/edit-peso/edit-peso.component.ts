import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { type_suino_peso } from '../../types/type_suino';
import { ApiService } from '../../services/api.service';
import { ActivatedRoute, Router } from '@angular/router';
import Swal from 'sweetalert2';
import { NgFor, NgIf } from '@angular/common';

@Component({
  selector: 'app-edit-peso',
  standalone: true,
  imports: [ReactiveFormsModule, NgIf, NgFor],
  templateUrl: './edit-peso.component.html',
  styleUrl: './edit-peso.component.css'
})
export class EditPesoComponent {
  SuinoPesoForm: FormGroup = new FormGroup({});
  suinoId: string = ""
  suinaPesoData: type_suino_peso | null = null

  constructor(private apiService: ApiService, private formBuilder: FormBuilder, private rotas: Router, private rota: ActivatedRoute) { }

  ngOnInit(): void {
    this.suinoId = this.rota.snapshot.params['id']
    this.SuinoPesoForm = this.formBuilder.group({
      'DataPesagem': [null, [Validators.required]],
      'suinoBrinco': [null],
      'suinoPeso': [null, [Validators.required]],
    })


    this.apiService.getPesoSuinoById(this.suinoId).subscribe((response) => {
      this.suinaPesoData = response;
    })

    setTimeout(() => {
      this.setFormValues()
    }, 1000)

  }
  setFormValues() {
    console.log("this.suinaPesoData", this.suinaPesoData)

    if (this.suinaPesoData !== null) {
      this.SuinoPesoForm.setValue(this.suinaPesoData);

    }

  }

  onSubmit(form: FormGroup) {
    if (this.SuinoPesoForm.valid) {


      this.apiService.editarPesoSuino(this.suinoId, form.value).subscribe(responseData => {
        Swal.fire({
          icon: 'success',
          title: 'Sucesso!',
          text: 'Peso atualizado com sucesso.',
          timer: 2000,
          showConfirmButton: false,
        });
        setTimeout(() => {
          this.SuinoPesoForm.reset()
          this.rotas.navigate([`/register-peso/${this.suinaPesoData!.suinoBrinco}`])

        }, 2500)
      });
    }
  }
}
