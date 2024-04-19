import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './components/header/header.component';
import { DestaquesComponent } from './components/destaques/destaques.component';
import { NoticiasComponent } from './components/noticias/noticias.component';
import { ResultadosComponent } from './components/resultados/resultados.component';
import { ServicosComponent } from './components/servicos/servicos.component';
import { FooterComponent } from './components/footer/footer.component';
import { MenuComponent } from './components/menu/menu.component';
import { HttpClientModule } from '@angular/common/http';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule,HttpClientModule, RouterOutlet, HeaderComponent,DestaquesComponent,NoticiasComponent,ResultadosComponent,ServicosComponent,NoticiasComponent,MenuComponent,FooterComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'UESC-app';
}
