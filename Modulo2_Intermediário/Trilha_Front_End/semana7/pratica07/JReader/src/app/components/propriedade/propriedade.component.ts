import { Component, EventEmitter, Input, Output } from '@angular/core';
import { type_veiculos } from '../../../types/types';
import { NgFor, NgIf } from '@angular/common';
import { VeiculosDirective } from '../../diretivas/veiculos.directive';

@Component({
  selector: 'app-propriedade',
  standalone: true,
  imports: [NgFor,NgIf, VeiculosDirective],
  templateUrl: './propriedade.component.html',
  styleUrl: './propriedade.component.css'
})
export class PropriedadeComponent {
  @Input() veiculo: any;
  @Output() propEscolhida = new EventEmitter<string>();
  
  selectProp(prop:string){
    this.propEscolhida.emit(prop);
  }

  obterChaves(): string[] {
    return Object.keys(this.veiculo);
  }
}
