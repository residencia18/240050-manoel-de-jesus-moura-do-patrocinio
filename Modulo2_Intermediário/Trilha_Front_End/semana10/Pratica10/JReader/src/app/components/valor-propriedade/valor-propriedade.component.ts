import { NgIf } from '@angular/common';
import { Component, Input } from '@angular/core';
import { ApiService } from '../../services/api-service.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-valor-propriedade',
  standalone: true,
  imports: [NgIf],
  templateUrl: './valor-propriedade.component.html',
  styleUrl: './valor-propriedade.component.css'
})
export class ValorPropriedadeComponent {
  valorPropriedade: string|null  = null;
  private dadosSubscription: Subscription;


  constructor(private apiServico: ApiService) {
    this.dadosSubscription = this.apiServico.getPropObservable().subscribe(
      data => {
        this.valorPropriedade = data
      },
      error => {
        console.log('Erro ao receber os dados do veiculo(propriedade):', error);
      }
    );
  }

  ngOnDestroy() {
    this.dadosSubscription.unsubscribe();
  }
}
