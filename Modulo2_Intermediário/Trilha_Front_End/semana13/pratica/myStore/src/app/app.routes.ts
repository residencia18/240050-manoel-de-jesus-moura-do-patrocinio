import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { RegisterAtendComponent } from './pages/register-atend/register-atend.component';
import { ListAtendComponent } from './pages/list-atend/list-atend.component';
import { EditAtendComponent } from './pages/edit-atend/edit-atend.component';
import { RegisterComponent } from './pages/register/register.component';

export const routes: Routes = [
    {path:"", component: HomeComponent},
    {path:"resgister-atend", component: RegisterAtendComponent},
    {path:"list-atend", component: ListAtendComponent},
    {path:"edit-atend/:id", component: EditAtendComponent},
    {path:"register", component: RegisterComponent},
    // {path:"login", component: EditAtendComponent},
];
