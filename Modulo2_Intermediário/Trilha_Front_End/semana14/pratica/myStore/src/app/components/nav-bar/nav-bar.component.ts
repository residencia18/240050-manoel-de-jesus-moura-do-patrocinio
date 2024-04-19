import { Component } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { Subscription } from 'rxjs';
import { AuthService } from '../../services/auth.service';
import { NgIf } from '@angular/common';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-nav-bar',
  standalone: true,
  imports: [RouterLink, NgIf],
  templateUrl: './nav-bar.component.html',
  styleUrl: './nav-bar.component.css'
})
export class NavBarComponent {
  private inscricao!: Subscription;
  isAuthenticated = false;

  constructor(private authService: AuthService, private router: Router) { }


  ngOnInit(): void {
    this.inscricao = this.authService.usuario.subscribe(
      usuario => {
        console.log(usuario.token);
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
