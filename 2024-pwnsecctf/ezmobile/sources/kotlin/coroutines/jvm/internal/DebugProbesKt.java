package kotlin.coroutines.jvm.internal;

import androidx.constraintlayout.core.motion.utils.TypedValues;
import kotlin.Metadata;
import kotlin.coroutines.Continuation;
import kotlin.jvm.internal.Intrinsics;

@Metadata(d1 = {"\u0000\u0012\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\u0002\n\u0002\b\u0003\u001a\"\u0010\u0000\u001a\b\u0012\u0004\u0012\u0002H\u00020\u0001\"\u0004\b\u0000\u0010\u00022\f\u0010\u0003\u001a\b\u0012\u0004\u0012\u0002H\u00020\u0001H\u0001\u001a\u0014\u0010\u0004\u001a\u00020\u00052\n\u0010\u0006\u001a\u0006\u0012\u0002\b\u00030\u0001H\u0001\u001a\u0014\u0010\u0007\u001a\u00020\u00052\n\u0010\u0006\u001a\u0006\u0012\u0002\b\u00030\u0001H\u0001¨\u0006\b"}, d2 = {"probeCoroutineCreated", "Lkotlin/coroutines/Continuation;", "T", "completion", "probeCoroutineResumed", "", "frame", "probeCoroutineSuspended", "kotlin-stdlib"}, k = 2, mv = {1, 8, 0}, xi = 48)
/* compiled from: DebugProbes.kt */
public final class DebugProbesKt {
    public static final <T> Continuation<T> probeCoroutineCreated(Continuation<? super T> continuation) {
        Intrinsics.checkNotNullParameter(continuation, "completion");
        return continuation;
    }

    public static final void probeCoroutineResumed(Continuation<?> continuation) {
        Intrinsics.checkNotNullParameter(continuation, TypedValues.AttributesType.S_FRAME);
    }

    public static final void probeCoroutineSuspended(Continuation<?> continuation) {
        Intrinsics.checkNotNullParameter(continuation, TypedValues.AttributesType.S_FRAME);
    }
}
