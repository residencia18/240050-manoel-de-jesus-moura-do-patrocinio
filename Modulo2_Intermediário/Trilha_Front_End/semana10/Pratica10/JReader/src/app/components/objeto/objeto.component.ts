import { NgFor, NgIf } from '@angular/common';
import { Component, EventEmitter, Input, Output } from '@angular/core';
import { type_veiculos, veiculosObj } from '../../../types/types';
import { VeiculosDirective } from '../../diretivas/veiculos.directive';
import { ApiService } from '../../services/api-service.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-objeto',
  standalone: true,
  imports: [NgFor, NgIf, VeiculosDirective],
  templateUrl: './objeto.component.html',
  styleUrl: './objeto.component.css'
})

export class ObjetoComponent {

  categoriaSelected: veiculosObj | null

  constructor(private apiServico: ApiService) {
    this.categoriaSelected = null

  }
 
  ngOnInit() {
    this.apiServico.getCategoriaObservable().subscribe(
      data => {
        this.categoriaSelected = data;
      },
      error => {
        console.log('Erro ao receber os dados:', error);
      }
    );
  }

  selectVeiculo(veiculo: type_veiculos) {

    this.apiServico.emitirVeiculo(veiculo);
  }


}
