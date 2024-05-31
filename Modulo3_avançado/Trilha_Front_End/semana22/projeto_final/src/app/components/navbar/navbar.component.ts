import { Component } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { Subscription } from 'rxjs';
import Swal from 'sweetalert2';
import { NgIf } from '@angular/common';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [RouterLink, NgIf],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent {
  private inscricao!: Subscription;
  isAuthenticated = false;

  constructor(private authService: AuthService, private router: Router) { }


  ngOnInit(): void {
    this.inscricao = this.authService.usuario.subscribe(
      usuario => {
        this.isAuthenticated = usuario.token == null ? false : true;
      });
  }

  ngOnDestroy(): void {
    this.inscricao.unsubscribe();
  }

  logout() {

    Swal.fire({
      icon: "question",
      text: "Tem certeza que deseja finalizar a sessão ?",
      showCancelButton: true,
      confirmButtonText: "Sair",
      denyButtonText: `Cancelar`
    }).then((result) => {
      if (result.isConfirmed) {
        this.authService.logout();
        Swal.fire("Até mais", "", "success").then(() => {
          this.router.navigate(['/']),
            window.location.reload()
        });
      }
    });
  }
}
