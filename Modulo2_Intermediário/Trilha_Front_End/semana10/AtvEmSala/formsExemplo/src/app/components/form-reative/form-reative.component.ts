import { NgIf } from '@angular/common';
import { Component } from '@angular/core';
import { AbstractControl, FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-form-reative',
  standalone: true,
  imports: [ReactiveFormsModule, NgIf],
  templateUrl: './form-reative.component.html',
  styleUrl: './form-reative.component.css'
})
export class FormReativeComponent {
  exemploForm: FormGroup;
 
 constructor() { 
    this.exemploForm = new FormGroup({
      'email': new FormControl(null, [Validators.required, Validators.minLength(10)]),
      'senha': new FormControl(null, [Validators.required, Validators.minLength(10), this.passwordValidator.bind(this)]), 
      'status': new FormControl(null, [this.statusValidator.bind(this)]), 
    })
  }

  onSubmit(){
    console.log(this.exemploForm);
    console.log(`${this.exemploForm.value.email}, ${this.exemploForm.value.senha}`);
  }

  passwordValidator(control: AbstractControl): 
  { [key: string]: boolean } | null {
    
    const value = control.value;
    if (value !== '1234' && value ) {
      return { 'invalidPassword': true };
    }
    return null;
  }

  statusValidator(control: AbstractControl): 
  { [key: string]: boolean } | null {
    
    const value = control.value;
    if (value !== 'valor1' && value ) {
      return { 'invalidStatus': true };
    }
    return null;
  }
}
