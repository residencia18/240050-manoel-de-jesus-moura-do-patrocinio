import { Component } from '@angular/core';
import { CommonModule, NgIf } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { ClasseComponent } from './components/classe/classe.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { type_veiculos, veiculosObj } from '../types/types';
import { ObjetoComponent } from './components/objeto/objeto.component';
import { PropriedadeComponent } from './components/propriedade/propriedade.component';
import { ValorPropriedadeComponent } from './components/valor-propriedade/valor-propriedade.component';
import { FooterComponent } from './components/footer/footer.component';
import { ApiService } from './services/api-service.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, NgIf, RouterOutlet, HttpClientModule,
    ClasseComponent, ObjetoComponent,
    PropriedadeComponent, ValorPropriedadeComponent,
    FooterComponent
  ],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService]
})
export class AppComponent {
  veiculo: type_veiculos | null = null;

  constructor(private apiServico: ApiService) {

    this.apiServico.getVeiculoObservable().subscribe(
      data => {
        this.veiculo = data

      },
      error => {
        console.log('Erro ao receber os dados do veiculo:', error);
      }
    );

  }

  addVeiculoOnList() {

    this.apiServico.emitirListaV(this.veiculo!.Name)

  }

  title = 'JReader';
}
