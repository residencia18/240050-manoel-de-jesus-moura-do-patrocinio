import { NgIf } from '@angular/common';
import { Component } from '@angular/core';
import { Subscription } from 'rxjs';
import { AuthService } from '../../services/auth.service';
import { Router, RouterLink } from '@angular/router';

@Component({
  selector: 'app-footer',
  standalone: true,
  imports: [NgIf, RouterLink],
  templateUrl: './footer.component.html',
  styleUrl: './footer.component.css'
})
export class FooterComponent {
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

}
