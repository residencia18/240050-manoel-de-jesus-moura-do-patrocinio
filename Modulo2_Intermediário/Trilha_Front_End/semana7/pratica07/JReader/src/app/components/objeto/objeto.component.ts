import { NgFor, NgIf } from '@angular/common';
import { Component, EventEmitter, Input, Output } from '@angular/core';
import { type_veiculos, veiculosObj } from '../../../types/types';
import { VeiculosDirective } from '../../diretivas/veiculos.directive';

@Component({
  selector: 'app-objeto',
  standalone: true,
  imports: [NgFor , NgIf,VeiculosDirective],
  templateUrl: './objeto.component.html',
  styleUrl: './objeto.component.css'
})

export class ObjetoComponent {
  @Input() veiculos:veiculosObj = {categoria:"",items:[]}
  @Output() veiculoEscolhida = new EventEmitter<type_veiculos>();
  
  selectVeiculo(veiculo:type_veiculos){
    this.veiculoEscolhida.emit(veiculo);

  }
}
