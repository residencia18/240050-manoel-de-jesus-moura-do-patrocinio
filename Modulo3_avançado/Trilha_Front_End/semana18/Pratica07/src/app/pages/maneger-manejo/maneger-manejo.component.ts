import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { FormArray, FormBuilder, FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { type_atividades, type_sessao } from '../../types/type_sessao';
import { NgFor, NgIf } from '@angular/common';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-maneger-manejo',
  standalone: true,
  imports: [ReactiveFormsModule, NgFor, NgIf],
  templateUrl: './maneger-manejo.component.html',
  styleUrl: './maneger-manejo.component.css'
})
export class ManegerManejoComponent {
  sessaoId: string = '';
  sessionData: type_sessao | null = null;
  editForm: FormGroup = new FormGroup({});
  animalFormArray: any

  constructor(private apiService: ApiService, private formBuilder: FormBuilder, private rota: ActivatedRoute) { }

  ngOnInit(): void {
    this.sessaoId = this.rota.snapshot.params['id'];
    this.editForm = this.formBuilder.group({
      's_date': [null, Validators.required],
      's_description': [null, Validators.required],
      s_animais: this.formBuilder.array([])
    });
    if (this.sessaoId.length > 0) {
      this.apiService.getSessaoById(this.sessaoId).subscribe((data) => {
        console.log('Dados da Sessão: ', data);
        this.sessionData = data;

      });
    }
    setTimeout(() => {
      this.initForm(this.sessionData!)

    }, 1000)
  }

  initForm(data: type_sessao) {
    this.editForm = this.formBuilder.group({
      s_date: [data.s_date],
      s_description: [data.s_description],
      s_animais: this.formBuilder.array([])
    });

    this.setAnimais(data.s_animais);
  }

  setAnimais(animais: any[]) {
    this.animalFormArray = this.editForm.get('s_animais') as FormArray;
    animais.forEach(animal => {
      const animalFormGroup = this.formBuilder.group({
        suinoBrinco: [animal.suinoBrinco],
        atividades: this.setAtividades(animal.atividades)
      });
      this.animalFormArray.push(animalFormGroup);
    });
    console.log('animalFormArray ', this.animalFormArray);
  }

  setAtividades(atividades: any[]) {
    const atividadeFormArray = new FormArray(
      atividades.map(atividade => this.formBuilder.group({
        atv_name: [atividade.atv_name],
        atv_status: [atividade.atv_status]
      }))
    );
    console.log('atividadeFormArray ', atividadeFormArray);

    return atividadeFormArray;
  }

  onSubmit(form: FormGroup) {
    console.log(this.editForm.value);

    if (this.editForm.valid) {

      this.apiService.editarSessao(this.sessaoId, form.value).subscribe(responseData => {
        Swal.fire({
          icon: 'success',
          title: 'Sucesso!',
          text: 'Sessão atualizada com sucesso.',
          timer: 2000,
          showConfirmButton: false,
        });
        setTimeout(() => {
          window.location.reload()
        }, 2500)
      });
    }
  }

}
