import { NgIf } from '@angular/common';
import { Component } from '@angular/core';
import { ReactiveFormsModule, FormGroup, FormBuilder, Validators } from '@angular/forms';
import { AuthService } from '../../services/auth.service';
import { Router, RouterLink } from '@angular/router';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-cadastro-usuario',
  standalone: true,
  imports: [ReactiveFormsModule, NgIf, RouterLink],
  templateUrl: './cadastro-usuario.component.html',
  styleUrl: './cadastro-usuario.component.css'
})
export class CadastroUsuarioComponent {
  registerForm: FormGroup = new FormGroup({});

  constructor(private authService: AuthService, private formBuilder: FormBuilder, private router: Router) { }

  ngOnInit(): void {
    this.registerForm = this.formBuilder.group({
      'user_email': [null, [Validators.required, Validators.email, Validators.minLength(10)]],
      'user_password': [null, [Validators.required, Validators.minLength(4), Validators.pattern(/^(?=.*[A-Z])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{4,}$/)]],

    })
  }
  onSubmit(form: FormGroup) {
    if (this.registerForm.valid) {
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
    }
  }

}
