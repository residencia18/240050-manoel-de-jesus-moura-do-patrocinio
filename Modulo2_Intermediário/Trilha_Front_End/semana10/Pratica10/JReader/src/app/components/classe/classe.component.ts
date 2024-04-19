import { Component, EventEmitter, Input, Output } from '@angular/core';
import { NgFor } from '@angular/common';
import { CategoriasDirective } from '../../diretivas/categorias.directive';
import { ApiService } from '../../services/api-service.service';

@Component({
  selector: 'app-classe',
  standalone: true,
  imports: [NgFor, CategoriasDirective],
  templateUrl: './classe.component.html',
  styleUrl: './classe.component.css'
})
export class ClasseComponent {
  categorias: string[]

  constructor(private apiServico: ApiService) {
    this.categorias = []
  }

  ngOnInit() {
    this.apiServico.getVeiculos().subscribe(
      dados => {
        this.categorias = Object.keys(dados)
      },
      error => {
        console.error("error ao carregar as categorias ", error)
      }
    )

  }



  selectCategoria(categoria: string) {
    this.apiServico.getVeiculos().subscribe(
      data => {
        this.apiServico.emitirCategoria({categoria:categoria, veiculos:data[categoria]});
      },
      error => {
        console.log('Erro ao carregar os dados da categoria:', error);
      }
    );

  }
}
