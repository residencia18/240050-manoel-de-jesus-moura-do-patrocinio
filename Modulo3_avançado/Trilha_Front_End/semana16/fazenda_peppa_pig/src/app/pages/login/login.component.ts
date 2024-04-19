import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { NgIf } from '@angular/common';
import { Router, RouterLink } from '@angular/router';
import Swal from 'sweetalert2';
// Importe o serviço de autenticação

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [ReactiveFormsModule, NgIf, RouterLink],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent {
  loginForm: FormGroup = new FormGroup({});

  constructor(private authService: AuthService, private formBuilder: FormBuilder, private router: Router) { }

  ngOnInit(): void {
    this.loginForm = this.formBuilder.group({
      'user_email': [null, [Validators.required, Validators.email, Validators.minLength(10)]],
      'user_password': [null, [Validators.required, Validators.minLength(4), Validators.pattern(/^(?=.*[A-Z])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{4,}$/)]],

    })
  }
  onSubmit(form: FormGroup) {

    if (this.loginForm.valid) {
      this.authService.loginUser(form.value.user_email, form.value.user_password).subscribe((res) => {
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
        text: 'Oppss... Houve um error no formulário, verifique os  campos e tente novamente.',
        showConfirmButton: true,

      })
      console.error('Por favor, corrija os erros no formulário.');
    }
  }
}
