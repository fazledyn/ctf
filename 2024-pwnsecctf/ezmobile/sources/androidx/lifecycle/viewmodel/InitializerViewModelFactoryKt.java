package androidx.lifecycle.viewmodel;

import androidx.lifecycle.ViewModel;
import androidx.lifecycle.ViewModelProvider;
import kotlin.Metadata;
import kotlin.Unit;
import kotlin.jvm.functions.Function1;
import kotlin.jvm.internal.Intrinsics;
import kotlin.jvm.internal.Reflection;

@Metadata(d1 = {"\u0000&\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\u001a%\u0010\u0000\u001a\u00020\u00012\u0017\u0010\u0002\u001a\u0013\u0012\u0004\u0012\u00020\u0004\u0012\u0004\u0012\u00020\u00050\u0003¢\u0006\u0002\b\u0006H\bø\u0001\u0000\u001a7\u0010\u0007\u001a\u00020\u0005\"\n\b\u0000\u0010\b\u0018\u0001*\u00020\t*\u00020\u00042\u0019\b\b\u0010\u0007\u001a\u0013\u0012\u0004\u0012\u00020\n\u0012\u0004\u0012\u0002H\b0\u0003¢\u0006\u0002\b\u0006H\bø\u0001\u0000\u0002\u0007\n\u0005\b20\u0001¨\u0006\u000b"}, d2 = {"viewModelFactory", "Landroidx/lifecycle/ViewModelProvider$Factory;", "builder", "Lkotlin/Function1;", "Landroidx/lifecycle/viewmodel/InitializerViewModelFactoryBuilder;", "", "Lkotlin/ExtensionFunctionType;", "initializer", "VM", "Landroidx/lifecycle/ViewModel;", "Landroidx/lifecycle/viewmodel/CreationExtras;", "lifecycle-viewmodel_release"}, k = 2, mv = {1, 8, 0}, xi = 48)
/* compiled from: InitializerViewModelFactory.kt */
public final class InitializerViewModelFactoryKt {
    public static final ViewModelProvider.Factory viewModelFactory(Function1<? super InitializerViewModelFactoryBuilder, Unit> function1) {
        Intrinsics.checkNotNullParameter(function1, "builder");
        InitializerViewModelFactoryBuilder initializerViewModelFactoryBuilder = new InitializerViewModelFactoryBuilder();
        function1.invoke(initializerViewModelFactoryBuilder);
        return initializerViewModelFactoryBuilder.build();
    }

    public static final /* synthetic */ <VM extends ViewModel> void initializer(InitializerViewModelFactoryBuilder initializerViewModelFactoryBuilder, Function1<? super CreationExtras, ? extends VM> function1) {
        Intrinsics.checkNotNullParameter(initializerViewModelFactoryBuilder, "<this>");
        Intrinsics.checkNotNullParameter(function1, "initializer");
        Intrinsics.reifiedOperationMarker(4, "VM");
        initializerViewModelFactoryBuilder.addInitializer(Reflection.getOrCreateKotlinClass(ViewModel.class), function1);
    }
}
