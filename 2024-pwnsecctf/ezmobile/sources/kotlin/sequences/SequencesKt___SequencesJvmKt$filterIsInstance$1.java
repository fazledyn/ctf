package kotlin.sequences;

import kotlin.Metadata;
import kotlin.jvm.functions.Function1;
import kotlin.jvm.internal.Lambda;

@Metadata(d1 = {"\u0000\u0012\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\u0010\u0000\u001a\u00020\u0001\"\u0004\b\u0000\u0010\u00022\b\u0010\u0003\u001a\u0004\u0018\u00010\u0004H\n¢\u0006\u0004\b\u0005\u0010\u0006"}, d2 = {"<anonymous>", "", "R", "it", "", "invoke", "(Ljava/lang/Object;)Ljava/lang/Boolean;"}, k = 3, mv = {1, 8, 0}, xi = 48)
/* compiled from: _SequencesJvm.kt */
final class SequencesKt___SequencesJvmKt$filterIsInstance$1 extends Lambda implements Function1<Object, Boolean> {
    final /* synthetic */ Class<R> $klass;

    /* JADX INFO: super call moved to the top of the method (can break code semantics) */
    SequencesKt___SequencesJvmKt$filterIsInstance$1(Class<R> cls) {
        super(1);
        this.$klass = cls;
    }

    public final Boolean invoke(Object obj) {
        return Boolean.valueOf(this.$klass.isInstance(obj));
    }
}
