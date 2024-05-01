import { NgFor, NgIf } from '@angular/common';
import { Component } from '@angular/core';
import { AbstractControl, FormControl, FormGroup, ReactiveFormsModule, ValidationErrors, Validators } from '@angular/forms';
import Swal from 'sweetalert2';
import { AuthService } from '../../services/auth.service';
import { type_user } from '../../types/user';
import { Router } from '@angular/router';

@Component({
  selector: 'formEvents',
  standalone: true,
  imports: [ReactiveFormsModule, NgIf, NgFor],
  templateUrl: './form.component.html',
  styleUrl: './form.component.css'
})
export class FormComponent {
  userForm: FormGroup;

  constructor(private authService: AuthService, private router: Router) {
    this.userForm = new FormGroup({
      'user_fistName': new FormControl(null, [Validators.required, Validators.maxLength(12), Validators.pattern(/^\S{1,12}$/)]),
      'user_fullName': new FormControl(null, [Validators.required, Validators.maxLength(25), this.validateFullName.bind(this)]),
      'user_password': new FormControl(null, [Validators.required, Validators.minLength(4), Validators.pattern(/^(?=.*[A-Z])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{4,}$/)]),
      'user_email': new FormControl(null, [Validators.required, Validators.email, Validators.minLength(10)]),
      'user_phone': new FormControl(null, [Validators.required, Validators.minLength(11), Validators.maxLength(14), Validators.pattern(/^\(\d{2}\)\d{5}-\d{4}$/)]),
      'user_address': new FormControl(null, [Validators.required, this.validateFullName.bind(this)]),
      'user_birthday': new FormControl(null, [Validators.required, this.validateBirthdate.bind(this)]),
      'user_gender': new FormControl(null, [Validators.required]),
      'user_profession': new FormControl(null, [Validators.required]),
    })
  }

  // personality validators
  validateFullName(control: AbstractControl): ValidationErrors | null {
    const value = control.value;
    if (value && value.trim().split(' ').length < 2) {
      return { invalidFullName: true };
    }
    return null;
  }


  validateBirthdate(control: AbstractControl) {
    const birthdate = new Date(control.value);
    const currentDate = new Date();
    const minAge = 18;
    if (!birthdate || isNaN(birthdate.getTime())) {
      return { invalidDate: true };
    }
    let age = currentDate.getFullYear() - birthdate.getFullYear();
    const monthDiff = currentDate.getMonth() - birthdate.getMonth();
    if (monthDiff < 0 || (monthDiff === 0 && currentDate.getDate() < birthdate.getDate())) {
      age--;
    }
    if (age < minAge) {
      return { minAge: true };
    }
    return null;
  }

  //end - personality validators

  onSubmit(form: FormGroup) {

    if (this.userForm.valid) {
      this.authService.signupUser(form.value.user_email, form.value.user_password).subscribe((res) => {
        Swal.fire({
          title: 'Sucesso !',
          icon: 'success',
          showConfirmButton: false,
          timer: 2000

        })
        setTimeout(() => {
          this.router.navigate(['/'])

        }, 2300)
      })

    } else {
      Swal.fire({
        title: 'Error !',
        icon: 'error',
        text: 'Oppss... Houve um error ao enviar o formulário, verifique os  campos e tente novamente.',
        showConfirmButton: true,

      })
      console.error('Por favor, corrija os erros no formulário.');
    }
  }

}
