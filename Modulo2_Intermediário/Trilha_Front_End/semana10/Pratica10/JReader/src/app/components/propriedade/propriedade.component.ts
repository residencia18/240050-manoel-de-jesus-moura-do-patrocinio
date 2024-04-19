import { Component, EventEmitter, Input, Output } from '@angular/core';
import { type_veiculos } from '../../../types/types';
import { NgFor, NgIf } from '@angular/common';
import { VeiculosDirective } from '../../diretivas/veiculos.directive';
import { ApiService } from '../../services/api-service.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-propriedade',
  standalone: true,
  imports: [NgFor, NgIf, VeiculosDirective],
  templateUrl: './propriedade.component.html',
  styleUrl: './propriedade.component.css'
})
export class PropriedadeComponent {
  veiculoProps: string[] | null = null;
  veiculo: any = null
  private dadosSubscription: Subscription;

  constructor(private apiServico: ApiService) {
    this.dadosSubscription = this.apiServico.getVeiculoObservable().subscribe(
      data => {
        this.veiculo = data
        this.veiculoProps = Object.keys(data);
      },
      error => {
        console.log('Erro ao receber os dados do veiculo(propriedade):', error);
      }
    );
  }
  selectProp(prop: any) {
    this.apiServico.emitirPropriedade(this.veiculo![prop]);

  }

  ngOnDestroy() {
    this.dadosSubscription.unsubscribe();
  }

}
