import { NgFor, NgIf } from '@angular/common';

import { Component, Input } from '@angular/core';
import { type_veiculos } from '../../../types/types';
import { ApiService } from '../../services/api-service.service';

@Component({
  selector: 'app-footer',
  standalone: true,
  imports: [NgFor, NgIf],
  templateUrl: './footer.component.html',
  styleUrl: './footer.component.css'
})
export class FooterComponent {
  veiculosSelecteds: string[] = []

  constructor(private apiServico: ApiService) {
    this.apiServico.getListObservable().subscribe(
      data => {
        !this.veiculosSelecteds.includes(data) && this.veiculosSelecteds.push(data);
      },
      error => {
        console.log('Erro ao receber os dados do veiculo adicionado:', error);
      }
    );
  }

  createJson() {
    return JSON.stringify(this.veiculosSelecteds, null, 2);

  }
}
