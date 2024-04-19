import { NgFor } from '@angular/common';

import { Component, Input } from '@angular/core';
import { type_veiculos } from '../../../types/types';

@Component({
  selector: 'app-footer',
  standalone: true,
  imports: [NgFor],
  templateUrl: './footer.component.html',
  styleUrl: './footer.component.css'
})
export class FooterComponent {
  @Input() veiculosSelecteds: type_veiculos[] = []

  createJson(){
    return JSON.stringify(this.veiculosSelecteds, null, 2);

  }
}
