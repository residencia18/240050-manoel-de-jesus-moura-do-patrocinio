import { Component, Input } from '@angular/core';
import { CommonModule, NgFor, NgIf } from '@angular/common';
import { AbstractControl, FormBuilder, FormControl, FormGroup, ReactiveFormsModule, ValidationErrors, Validators } from '@angular/forms';
import { ApiService } from '../../services/api.service';
import { type_atendimento } from '../../types/atendimento';
import { Router } from '@angular/router';

@Component({
  selector: 'app-form-atendimento',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, NgIf, NgFor],
  templateUrl: './form-atendimento.component.html',
  styleUrl: './form-atendimento.component.css'
})
export class FormAtendimentoComponent {

  @Input() formDataToEdit: type_atendimento | null = null;

  formAtendimento: FormGroup = new FormGroup({});

  constructor(private apiService: ApiService, private formBuilder: FormBuilder,private rotas:Router) { }

  ngOnInit(): void {
    this.formAtendimento = this.formBuilder.group({
      'user_fullName': [null, [Validators.required, Validators.maxLength(90), this.validateFullName.bind(this)]],
      'user_email': [null, [Validators.required, Validators.email, Validators.minLength(10)]],
      'user_phone': [null, [Validators.required, Validators.minLength(11), Validators.maxLength(14), Validators.pattern(/^\(\d{2}\)\d{5}-\d{4}$/)]],
      'user_address': [null, [Validators.required, this.validateFullName.bind(this)]],
      'atend_type_pet': [null, [Validators.required]],
      'atend_name_pet': [null, [Validators.required]],
      'atend_age_pet': [null, [Validators.required]],
      'atend_date': [null, [Validators.required]],
      'atend_hour': [null, [Validators.required]],
    });

    setTimeout(()=>{
      this.setFormValues()
    },2000)
  }

  
  setFormValues(){
    console.log("formDataToEdit", this.formDataToEdit )
    if (this.formDataToEdit !== null) {
      this.formAtendimento.setValue(this.formDataToEdit);
      Object.keys(this.formAtendimento.controls).forEach(controlName => {
        this.formAtendimento.get(controlName)?.markAsTouched();
      });
    }
 
  }


  // personality validators
  validateFullName(control: AbstractControl): ValidationErrors | null {
    const value = control.value;
    if (value && value.trim().split(' ').length < 2) {
      return { invalidFullName: true };
    }
    return null;
  }

  //end - personality validators

  onSubmit(form:any) {

    if (this.formDataToEdit !== null) {
      this.apiService.editarAtendimento(this.formDataToEdit?.id!, form.value);

    } else {
   
      this.apiService.addAtendimento(form.value);
    }
   
    this.rediracionaPrincipal()
  }

  rediracionaPrincipal(){
    setTimeout(() => {
     this.rotas.navigate(['list-atend']);
    }, 2000);
    
  }
}
